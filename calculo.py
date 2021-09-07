cores = {'brancoeazul':'\033[30;44m',
         'vermelhoebranco':'\033[31;40m',
         'amarelo': '\033[33m',
         'verdeeamarelo': '\033[33;42m'}

real = float(input('Quantos reais você tem? R$ '))
local = input('Para qual país da América do sul você quer ir? ').strip()
pesochile = real * 150.57  #Chile
pesoargentina = real * 18.95  #Argentina
pesouruguaio = real* 8.24  #Uruguai
guarani = real * 133.78  #Paraguai
dolarsuriname = real * 0.24  #Suriname
usdolar = real * 0.19  #Equador
boliviano = real * 1.33  #Bolívia
pesocolombiano = real * 736.38  #Colômbia
novosol = real * 0.79  #Peru
dolarguiana = real * 0.025  #Guiana
euroguianafrancesa = real * 0.16  #Guiana francesa
bolivarvenezuelano = real * 789067.72  #Venezuela
if local.upper() == 'BRASIL':
      print(cores['verdeeamarelo'], 'Com o valor de R${:.2f} Reais você podo visitar:\033[m'.format(real))
      if real >= 100:
            print(cores['verdeeamarelo'], '- O parque lage por: 100 reais.\033[m')
      else:
            print(cores['verdeeamarelo'], '- O piscinão de ramos e comprar um espetinho e uma brahma.\033[m')

if local.upper() == 'ARGENTINA':
      print(cores['brancoeazul'], 'Com seu dinheiro você pode comprar: ${:.2f} pesos argentinos.\033[m'.format(pesoargentina))
      if real >= 214:
            print(cores['brancoeazul'], 'Você pode degustar vinhos conhecendo uma vinícola em Mendoza por: $214,00.\033[m')
      else:
            print(cores['brancoeazul'], 'Você pode dar um rolê por Buenos aires de bicicleta.\033[m')
if local.upper() == 'URUGUAI':
      print(cores['brancoeazul'], 'Com seu dinheiro você pode comprar:\{:.2f} Pesos uruguaios.\033[m'.format(pesouruguaio))
      if real >= 319:
            print(cores['brancoeazul'], 'Conheça a Colônia do Sacramento por: $319,00.\033[m')
      else:
            print(cores['brancoeazul'], 'Vá ao Pub Crawl Montevidéu, com valores à partir de $109.00.\033[m')
if local.upper() == 'PARAGUAI':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Guaranis.\033[m'.format(guarani))
      if real >= 640:
            print(cores['vermelhoebranco'], 'Você pode ir às Cataratas de Cristal por: ₲640.00.\033[m')
      else:
            print(cores['vermelhoebranco'], 'Você pode fazer um tour pelas missões jesuísticas por ₲\033[m')
if local.upper() == 'SURINAME':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Dolares do Suriname.'.format(dolarsuriname))
      if real >= 550:
            print('Faça uma excursão pelas Ruines of Jodensavanne.\033[m')
      else:
            print('Faça uma City tour por R$170 reais.\033[m')
if local.upper() == 'EQUADOR':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Dolares \033[m'.format(usdolar))
      if real >= 1300:
            print('O melhor passeio a se fazer é visitar as ilhas Galápagos e fazer um mergulho pela paissagem deslumbrante por R$1,300.\033[m')
      else:
            print('Um ótimo passeio é ir nas Termas de Papallacta por R$472,73.\033[m')

      print('''Curiosidade: O Equador adotou o dólar como moeda para recuperar a economia do país, já que por volta do ano 1999 o
 Equador apresentava inflação e desvalorização do Sucre Equatoriano que era a moeda na época. Com essa mudança foi
 possível o país equilibrar a economia e conter a inflação.''')
if local.upper() == 'BOLÍVIA':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(boliviano))
      if real >= 137:
            print('Passeio de esqui pela geleira de  Chalcataya por R$136,24')
      else:
            print('Excursão histórica pela cidade de La Paz por R$26,56')
if local.upper() == 'COLÔMBIA':
          print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(pesocolombiano))
          if real >= 473:
                print('Você pode fazer uma excursão turística à cidade de Bogotá com passeio de teleférico por R$472,73')
          else:
                print('Seja um Aquanauta em um mergulho pelo litoral de San Andrés por R$185,90')
if local.upper() == 'PERU':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(novosol))
      if real >= 218:
            print('Você pode ter uma experiência gastronômica com um chef em Mancora por R$217,93')
      else:
            print('Conheça Machupicchu com um guia por R$216,55')
if local.upper() == 'GUIANA':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(dolarguiana))
      if real >= 1450:
            print('Hospede-se no Guyana Marriott Hotel Georgetown por R$1.450')
      else:
            print('Faça uma excursão de curry em Georgetown por R$663,94')
if local.upper() == 'GUIANA FRANCESA':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(euroguianafrancesa))
if local.upper() == 'VENEZUELA':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(bolivarvenezuelano))
if local.upper() == 'CHILE':
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(pesochile))
      if real >= 1200:
            print('Faça uma excursão de bicicleta de dia inteiro no Vale do Maipo e degustação de vinhos de Santiago por R$1.046,38')
      else:
            print('Faça um passeio com um guia pelo Vulcão Osorno e pelas Cataratas Petrohué por R$212,46')
