import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO ---
ARQUIVO_DADOS = 'transacoes_mock.csv'

# --- FUNÇÃO PRINCIPAL ---
def analisar_fraude():
    print("🔄 Carregando base de dados...")
    try:
        df = pd.read_csv(ARQUIVO_DADOS)
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{ARQUIVO_DADOS}' não encontrado.")
        return

    # Converter coluna de hora para número
    df['hora'] = pd.to_numeric(df['hora'])

    # --- REGRA DE NEGÓCIO (COMPLIANCE) ---
    # Política: Aprovações manuais são PROIBIDAS entre 00h e 05h.
    print("🔍 Auditando regras de horário (Janela 00h-05h)...")
    
    # Filtrar transações suspeitas (Flag)
    anomalias = df[(df['hora'] >= 0) & (df['hora'] <= 5)]
    
    quantidade_anomalias = len(anomalias)

    if quantidade_anomalias > 0:
        print(f"⚠️  RISCO DETECTADO: {quantidade_anomalias} aprovações fora da janela operacional!")
        gerar_grafico(df)
    else:
        print("✅ Nenhuma violação de compliance detectada.")

def gerar_grafico(df):
    print("📊 Gerando evidência visual...")
    
    # Agrupar por hora para contagem
    volume_por_hora = df.groupby('hora').size()
    
    # Plotar
    plt.figure(figsize=(10, 6))
    cores = ['red' if (h >= 0 and h <= 5) else '#1f77b4' for h in volume_por_hora.index]
    
    plt.bar(volume_por_hora.index, volume_por_hora.values, color=cores)
    plt.title('Análise de Anomalia: Volume de Aprovações por Hora', fontsize=14, fontweight='bold')
    plt.xlabel('Hora do Dia (0h - 23h)')
    plt.ylabel('Quantidade de Transações')
    plt.xticks(range(0, 24))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adicionar anotação de alerta
    plt.text(0, max(volume_por_hora.values), '⚠️ ALERTA: Pico Incomum (3 AM)', color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('evidencia_fraude.png')
    print("✅ Gráfico salvo como 'evidencia_fraude.png'")

if __name__ == "__main__":
    analisar_fraude()
