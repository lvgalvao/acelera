# Teste Técnico SQL 02 – Stored Procedures

## Contexto do Sistema

Você está modelando um **sistema acadêmico simplificado** para uma universidade.
O banco de dados contém:

* **alunos** → pessoas matriculadas na instituição
* **cursos** → cada aluno pertence a um curso (ex.: Sistemas, Engenharia)
* **materias** → disciplinas vinculadas a um curso (ex.: Banco de Dados, Programação)
* **matricula** → registro de que um aluno está cursando determinada matéria em um determinado ano letivo

Esse cenário é clássico em sistemas de ensino e ajuda a entender como organizar relacionamentos **1:N** e **N:N** no banco.

---

## Estrutura das Tabelas

```sql
CREATE TABLE alunos (
    matricula SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE cursos (
    curso CHAR(3) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE materias (
    sigla CHAR(3) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    curso CHAR(3) REFERENCES cursos(curso)
);

CREATE TABLE matricula (
    matricula INT REFERENCES alunos(matricula),
    curso CHAR(3) REFERENCES cursos(curso),
    materia CHAR(3) REFERENCES materias(sigla),
    perletivo INT,
    PRIMARY KEY (matricula, materia, perletivo)
);
```

---

## Inserts de Exemplo

```sql
INSERT INTO alunos (nome) VALUES ('Pedro'), ('Maria');

INSERT INTO cursos (curso, nome) 
VALUES ('SIS','Sistemas'), ('ENG','Engenharia');

INSERT INTO materias (sigla, nome, curso) 
VALUES 
('BDA', 'Banco de Dados', 'SIS'),
('PRG', 'Programação', 'SIS'),
('MAT', 'Matemática', 'ENG');
```

---

## Objetivo do Exercício

Criar uma **Stored Procedure** chamada `sp_matricula_aluno` que:

1. Recebe como parâmetros o **nome do aluno** e o **nome do curso**.
2. Descobre automaticamente o `matricula` do aluno e o `curso` informado.
3. Insere registros de matrícula em **todas as matérias** vinculadas ao curso, usando o **ano letivo atual**.
4. Garante que não haja duplicação de registros.

---

## Comandos Importantes que você vai usar

1. **SELECT ... INTO** → buscar valores de uma tabela e armazenar em variáveis.
2. **IF / RAISE EXCEPTION** → validar condições e retornar erros amigáveis.
3. **INSERT INTO ... SELECT** → inserir várias linhas de uma vez, baseadas em outra tabela.
4. **ON CONFLICT DO NOTHING** → evitar duplicações no `INSERT`.
5. **GET DIAGNOSTICS / RAISE NOTICE** → mostrar mensagens sobre quantas linhas foram inseridas.

---

## Exemplo de Uso

```sql
-- Matricular Pedro no curso de Sistemas (ano atual)
CALL sp_matricula_aluno('Pedro', 'Sistemas');

-- Consultar resultado
SELECT * FROM matricula;
```

### Resultado esperado:

Pedro aparece matriculado em todas as matérias do curso de **Sistemas**:

* Banco de Dados (BDA)
* Programação (PRG)

---

## Gabarito – Procedure `sp_matricula_aluno`

```sql
CREATE OR REPLACE PROCEDURE sp_matricula_aluno(
    p_nome_aluno  VARCHAR,
    p_nome_curso  VARCHAR,
    p_perletivo   INT DEFAULT EXTRACT(YEAR FROM CURRENT_DATE)
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_matricula INT;
    v_curso     CHAR(3);
    v_qtd       INT;
BEGIN
    -- Busca o aluno
    SELECT a.matricula INTO v_matricula
    FROM alunos a
    WHERE a.nome = p_nome_aluno;

    IF v_matricula IS NULL THEN
        RAISE EXCEPTION 'Aluno "%" não encontrado', p_nome_aluno;
    END IF;

    -- Busca o curso
    SELECT c.curso INTO v_curso
    FROM cursos c
    WHERE c.nome = p_nome_curso;

    IF v_curso IS NULL THEN
        RAISE EXCEPTION 'Curso "%" não encontrado', p_nome_curso;
    END IF;

    -- Matricula o aluno em todas as matérias do curso
    INSERT INTO matricula (matricula, curso, materia, perletivo)
    SELECT v_matricula, m.curso, m.sigla, p_perletivo
    FROM materias m
    WHERE m.curso = v_curso
    ON CONFLICT (matricula, materia, perletivo) DO NOTHING;

    GET DIAGNOSTICS v_qtd = ROW_COUNT;
    RAISE NOTICE 'Aluno "%": % matérias matriculadas no curso "%" para o ano %',
                  p_nome_aluno, v_qtd, p_nome_curso, p_perletivo;
END;
$$;
```