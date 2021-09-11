from time import sleep
import emoji
cores = {'brancoeazul': '\033[30;44m',
         'vermelhoebranco': '\033[31;40m',
         'amarelo': '\033[33m',
         'verdeeamarelo': '\033[33;42m'}

local = input('Para qual país da América do sul você quer ir? ').strip()
real = float(input('Quantos reais você tem? R$ '))

pesochile = 150.57  #Chile
pesoargentina = 18.41  #Argentina
pesouruguaio = 8.24  #Uruguai
guarani = 133.78  #Paraguai
dolarsuriname = 0.24  #Suriname
usdolar = 0.19  #Equador
boliviano = 1.33  #Bolívia
pesocolombiano = 736.38  #Colômbia
novosol = 0.79  #Peru
dolarguiana = 0.025  #Guiana
euroguianafrancesa = 0.16  #Guiana francesa
bolivarvenezuelano = 789067.72  #Venezuela

if local.upper() == 'BRASIL':
      print(emoji.emojize('🇧🇷', use_aliases=True))
      sleep(1)
      print(cores['verdeeamarelo'], 'Com o valor de R${:.2f} Reais você pode visitar:\033[m'.format(real))
      sleep(1)
      if real >= 100:
            print(cores['verdeeamarelo'], 'O Cristo redentor por:R$83,50, mais alimentação.\033[m')
      else:
            print(cores['verdeeamarelo'], 'O parque lage por: R$10,00, mais alimentação.\033[m')

if local.upper() == 'ARGENTINA':
      print(emoji.emojize('🇦🇷', use_aliases=True))
      sleep(1)
      print(cores['brancoeazul'], 'Com seu dinheiro você pode comprar: ${:.2f} pesos argentinos.\033[m'.format(pesoargentina * real))
      sleep(1)
      if real >= 214:
            print(cores['brancoeazul'], 'Você pode degustar vinhos conhecendo uma vinícola em Mendoza por: ${:.2f}.\033[m'.format(214 * pesoargentina))
      else:
            print(cores['brancoeazul'], 'Você pode dar um rolê por Buenos aires de bicicleta por: ${}.\033[m'.format(pesoargentina))
if local.upper() == 'URUGUAI':
      print(emoji.emojize('🇺🇾', use_aliases=True))
      sleep(1)
      print(cores['brancoeazul'], 'Com seu dinheiro você pode comprar:{:.2f} Pesos uruguaios.\033[m'.format(pesouruguaio * real))
      sleep(1)
      if real >= 319:
            print(cores['brancoeazul'], 'Conheça a Colônia do Sacramento por: ${:.2f}.\033[m'.format(pesouruguaio * 319))
      else:
            print(cores['brancoeazul'], 'Vá ao Pub Crawl Montevidéu, com valores à partir de ${:.2f}.\033[m'.format(pesouruguaio * 109))
if local.upper() == 'PARAGUAI':
      print(emoji.emojize('🇵🇾', use_aliases=True))
      sleep(1)
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Guaranis.\033[m'.format(guarani))
      sleep(1)
      if real >= 640:
            print(cores['vermelhoebranco'], 'Você pode ir às Cataratas de Cristal por: ₲{:.2f}.\033[m'.format(guarani * 640))
      else:
            print(cores['vermelhoebranco'], 'Você pode fazer um tour pelas missões jesuísticas por ₲{:.2f}\033[m'.format(guarani))
if local.upper() == 'SURINAME':
      print(emoji.emojize('🇸🇷', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Dolares do Suriname.'.format(dolarsuriname * real))
      sleep(1)
      if real >= 550:
            print('Faça uma excursão pelas Ruines of Jodensavanne por: ${:.2f}.\033[m'.format(dolarsuriname * 550))
      else:
            print('Faça uma City tour por ${:.2f}.\033[m'.format(dolarsuriname * 170))
if local.upper() == 'EQUADOR':
      print(emoji.emojize('🇪🇨', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} Dolares \033[m'.format(usdolar * real))
      sleep(1)
      if real >= 1300:
            print('O melhor passeio a se fazer é visitar as ilhas Galápagos e fazer um mergulho pela paissagem deslumbrante por ${:.2f}.\033[m'.format(usdolar * 1.300))
      else:
            print('Um ótimo passeio é ir nas Termas de Papallacta por ${:.2f}.\033[m'.format(usdolar * 472.73))
      sleep(2)
      print('''Curiosidade: O Equador adotou o dólar como moeda para recuperar a economia do país, já que por volta do ano 1999 o
 Equador apresentava inflação e desvalorização do Sucre Equatoriano que era a moeda na época. Com essa mudança foi
 possível o país equilibrar a economia e conter a inflação.''')
if local.upper() == 'BOLÍVIA':
      print(emoji.emojize('🇧🇴', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(boliviano * real))
      sleep(1)
      if real >= 137:
            print('Passeio de esqui pela geleira de  Chalcataya por ${:.2f}'.format(boliviano * 136.24))
      else:
            print('Excursão histórica pela cidade de La Paz por ${:.2f}'.format(boliviano * 26.56))
if local.upper() == 'COLÔMBIA':
          print(emoji.emojize('🇨🇴', use_aliases=True))
          print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(pesocolombiano * real))
          sleep(1)
          if real >= 473:
                print('Você pode fazer uma excursão turística à cidade de Bogotá com passeio de teleférico por ${:.2f}'.format(pesocolombiano * 472.73))
          else:
                print('Seja um Aquanauta em um mergulho pelo litoral de San Andrés por ${:.2f}'.format(pesocolombiano * 185.90))
if local.upper() == 'PERU':
      print(emoji.emojize('🇵🇪', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\nS/{:.2f} '.format(novosol * real))
      sleep(1)
      if real >= 218:
            print('Você pode ter uma experiência gastronômica com um chef em Mancora por S/{:.2f}'.format(novosol * 217.93))
      else:
            print('Conheça Machupicchu com um guia por S/{:.2f}'.format(novosol * 216.55))
if local.upper() == 'GUIANA':
      print(emoji.emojize('🇬🇾', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(dolarguiana * real))
      sleep(1)
      if real >= 1450:
            print('Hospede-se no Guyana Marriott Hotel Georgetown por ${:.2f}'.format(dolarguiana * 1450))
      else:
            print('Faça uma excursão de curry em Georgetown por ${:.2f}'.format(dolarguiana * 663.94))
if local.upper() == 'GUIANA FRANCESA':
      print(emoji.emojize('🇬🇫', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(euroguianafrancesa * real))
if local.upper() == 'VENEZUELA':
      print(emoji.emojize('🇻🇪', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(bolivarvenezuelano * real))
if local.upper() == 'CHILE':
      print(emoji.emojize('🇨🇱', use_aliases=True))
      print(cores['vermelhoebranco'], 'Com seu dinheiro você pode comprar:\n{:.2f} '.format(pesochile * real))
      sleep(1)
      if real >= 1200:
            print('Faça uma excursão de bicicleta de dia inteiro no Vale do Maipo e degustação de vinhos de Santiago por ${:.2f}'.format(pesochile * 1046.38))
      else:
            print('Faça um passeio com um guia pelo Vulcão Osorno e pelas Cataratas Petrohué por ${:.2f}'.format(pesochile * 212.46))
