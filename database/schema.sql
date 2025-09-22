-- Tabela para armazenar respostas do questionário
CREATE TABLE IF NOT EXISTS respostas_questionario (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    respostas JSONB NOT NULL,
    trilhas_recomendadas JSONB NOT NULL,
    trilhas_nomes JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Índices para melhorar performance
CREATE INDEX IF NOT EXISTS idx_respostas_questionario_created_at ON respostas_questionario(created_at);
CREATE INDEX IF NOT EXISTS idx_respostas_questionario_timestamp ON respostas_questionario(timestamp);

-- Índice GIN para busca em campos JSONB
CREATE INDEX IF NOT EXISTS idx_respostas_questionario_respostas ON respostas_questionario USING GIN(respostas);
CREATE INDEX IF NOT EXISTS idx_respostas_questionario_trilhas ON respostas_questionario USING GIN(trilhas_recomendadas);

-- Função para atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger para atualizar updated_at automaticamente
CREATE TRIGGER update_respostas_questionario_updated_at 
    BEFORE UPDATE ON respostas_questionario 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- Comentários na tabela e colunas
COMMENT ON TABLE respostas_questionario IS 'Tabela para armazenar respostas do questionário de orientação';
COMMENT ON COLUMN respostas_questionario.id IS 'ID único da resposta';
COMMENT ON COLUMN respostas_questionario.timestamp IS 'Timestamp da resposta (ISO format)';
COMMENT ON COLUMN respostas_questionario.respostas IS 'Respostas do questionário em formato JSON';
COMMENT ON COLUMN respostas_questionario.trilhas_recomendadas IS 'IDs das trilhas recomendadas';
COMMENT ON COLUMN respostas_questionario.trilhas_nomes IS 'Nomes das trilhas recomendadas';
COMMENT ON COLUMN respostas_questionario.created_at IS 'Data de criação do registro';
COMMENT ON COLUMN respostas_questionario.updated_at IS 'Data da última atualização do registro';
