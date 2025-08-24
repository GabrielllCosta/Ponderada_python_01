import pandas as pd 

df = pd.read_csv("Ponderada_programacao/adult_data.csv")

def densidade_demografica(df):
   # Contagem de pessoas por raça
   contagem_raca = df['race'].value_counts()

    # Idade média dos homens
   idade_media_homens = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentagem de pessoas com diploma de bacharel
   porcetagem_bacharel = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Educação avançada
   educacao_avancada = ['Bachelors', 'Masters', 'Doctorate']
   edu_alta = df[df['education'].isin(educacao_avancada)]
   porcentagem_rica = round(( edu_alta['salary'] == '>50K').mean() * 100,1)
   
   # Pessoas sem educação avançada
   edu_baixa = df[~df['education'].isin(educacao_avancada)]
   porcetagem_pobre = round((edu_baixa['salary'] == '>50K').mean() * 100, 1)

   # Número mínimo de horas trabalhadas
   min_horas = df['hours-per-week'].min()

   # Porcetagem que trabalha o mínimo e gnaha mais de 50K
   min_trabalhadores= df[df['hours-per-week'] == min_horas]
   porcetagem_min_trabalhadores = round((min_trabalhadores['salary'] == '50K').mean() * 100, 1)

   # País com maior porcentagem de pessoas que ganham >50K
   salario_pais = df[df['salary'] == '>50K']['native-country'].value_counts()
   total_pais = df['native-country'].value_counts()
   pais_porcetagem = (salario_pais/ total_pais * 100).round(1)
   pais_alto = pais_porcetagem.idxmax()
   pais_alto_porcetagem =  pais_porcetagem.max()

    # Ocupação mais popular para quem ganha >50K na Índia
   ocupacao_alta = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

   return {
        "contagem_raca": contagem_raca,
        "idade_media_homens": idade_media_homens,
        "porcentagem_bacharel": porcetagem_bacharel,
        "porcentagem_rica_edu_avancada": porcentagem_rica,
        "porcentagem_rica_edu_baixa": porcetagem_pobre,
        "min_horas": min_horas,
        "porcentagem_min_trabalhadores": porcetagem_min_trabalhadores,
        "pais_alto": pais_alto,
        "pais_alto_porcetagem": pais_alto_porcetagem,
        "ocupacao_mais_popular_india": ocupacao_alta
    }

resultado = densidade_demografica(df)
print(resultado)

