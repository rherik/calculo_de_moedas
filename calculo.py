from time import sleep
import emoji
cores = ('\033[7;44m',        #Azul
         '\033[31;47m',       #Vermelho
         '\033[33;7m',       #Amarelo
         '\033[33;42m')       #Amarelo e verde
local = input('Para qual país da América do sul você quer ir? ').strip()
sleep(1)
print(f'{emoji.emojize(" 🇧🇷", use_aliases=True)} - {emoji.emojize("🇦🇷", use_aliases=True)} - '
      f'{emoji.emojize("🇺🇾", use_aliases=True)} - {emoji.emojize("🇵🇾", use_aliases=True)} - '
      f'{emoji.emojize("🇸🇷", use_aliases=True)} - {emoji.emojize("🇪🇨", use_aliases=True)} - '
      f'{emoji.emojize("🇧🇴", use_aliases=True)} - {emoji.emojize("🇨🇴", use_aliases=True)} - '
      f'{emoji.emojize("🇵🇪", use_aliases=True)} - {emoji.emojize("🇬🇾", use_aliases=True)} - '
      f'{emoji.emojize("🇬🇫", use_aliases=True)} - {emoji.emojize("🇻🇪", use_aliases=True)} - '
      f'{emoji.emojize("🇨🇱", use_aliases=True)}' * 5)
sleep(1)
real = float(input('Quantos reais você tem? R$ '))
paises = ['ARGENTINA', 18.41, 'BOLÍVIA', 1.33, 'CHILE', 150.57, 'COLÔMBIA', 736.38, 'EQUADOR', 0.19, 'GUIANA', 0.025,
          'GUIANA FRANCESA', 0.16, 'PARAGUAI', 133.78, 'PERU', 0.79, 'SURINAME', 0.24, 'URUGUAI', 8.24, 'VENEZUELA',
          789067.72]

#Valores dentro de format nos if's/else's são os preços em reais para a devida conversão para a moeda local.

if local.upper() == 'BRASIL':
      sleep(1)
      print(cores[3], f'Com o valor de R${real:.2f} Reais você podo visitar:\033[m')
      sleep(1)
      if real >= 100:
            print(cores[3], 'O Cristo redentor por:\nR$83,50, mais alimentação.\033[m')
      else:
            print(cores[3], 'O parque lage por:\nR$10,00, mais alimentação.\033[m')

if local.upper() == 'ARGENTINA':
      sleep(1)
      print(cores[0],
            f'Com seu dinheiro você pode comprar:${paises[1] * real:.2f} pesos argentinos.\033[m')
      sleep(1)
      if real >= 214:
            print(cores[0],
                  f'Você pode degustar vinhos conhecendo uma vinícola em Mendoza por:${214 * paises[1]:.2f}.\033[m')
      else:
            print(cores[0],
                  f'Você pode dar um rolê por Buenos aires de bicicleta por:${paises[1]:.2f}.\033[m')

if local.upper() == 'BOLÍVIA':
      print(cores[1], f'Com seu dinheiro você pode comprar:\n${paises[3] * real:.2f}\033[m')
      sleep(1)
      if real >= 137:
            print(cores[1], f'Passeio de esqui pela geleira de  Chalcataya por:${paises[3] * 136.24:.2f}\033[m')
      else:
            print(cores[1], f'Excursão histórica pela cidade de La Paz por:${paises[3] * 26.56:.2f}\033[m')

if local.upper() == 'CHILE':
      print(cores[1], f'Com seu dinheiro você pode comprar:${paises[5] * real:.2f}\033[m')
      sleep(1)
      if real >= 1200:
            print(cores[1], f'Faça uma excursão de bicicleta de dia inteiro no Vale do Maipo e degustação de vinhos de Santiago '
                  f'por:${paises[5] * 1046.38:.2f}\033[m')
      else:
            print(cores[1], f'Faça um passeio com um guia pelo Vulcão Osorno e pelas Cataratas Petrohué '
                  f'por:${paises[5] * 212.46:.2f}\033[m')

if local.upper() == 'COLÔMBIA':
          print(cores[1],
                f'Com seu dinheiro você pode comprar:${paises[7] * real:.2f}\033[m')
          sleep(1)
          if real >= 473:
                print(cores[1], f'Você pode fazer uma excursão turística à cidade de Bogotá com passeio de teleférico '
                      f'por:${paises[7] * 472.73:.2f}\033[m')
          else:
                print(cores[1], f'Seja um Aquanauta em um mergulho pelo litoral de San Andrés '
                                f'por:${paises[7] * 185.90:.2f}\033[m')

if local.upper() == 'EQUADOR':
      print(cores[1], f'Com seu dinheiro você pode comprar:${paises[9] * real:.2f} Dolares \033[m')
      sleep(1)
      if real >= 1300:
            print(cores[1], f'O melhor passeio a se fazer é visitar as ilhas Galápagos e fazer um mergulho '
                  f'pela paissagem deslumbrante por:${paises[9] * 1.300:.2f}.\033[m')
      else:
            print(cores[1], f'Um ótimo passeio é ir nas Termas de Papallacta por:${paises[9] * 472.73:.2f}.\033[m')
      sleep(2)
      print(cores[1], '''Curiosidade: O Equador adotou o dólar como moeda para recuperar a economia do país, já que por volta 
      do ano 1999 o Equador apresentava inflação e desvalorização do Sucre Equatoriano que era a moeda na época. 
      Com essa mudança foi possível o país equilibrar a economia e conter a inflação.\033[m''')

if local.upper() == 'GUIANA':
      print(cores[1], f'Com seu dinheiro você pode comprar:\n${paises[11] * real:.2f}\033[m')
      sleep(1)
      if real >= 1450:
            print(f'Hospede-se no Guyana Marriott Hotel Georgetown por:\n${paises[11] * 1450:.2f}')
      else:
            print(f'Faça uma excursão de curry em Georgetown por:\n${paises[11] * 663.94:.2f}')

if local.upper() == 'GUIANA FRANCESA':
      print(cores[1], f'Com seu dinheiro você pode comprar:\n${paises[13] * real:.2f}\033[m')

if local.upper() == 'PARAGUAI':
      sleep(1)
      print(cores[1], f'Com seu dinheiro você pode comprar:\n₲{paises[15] * real:.2f} Guaranis.\033[m')
      sleep(1)
      if real >= 640:
            print(cores[1], f'Você pode ir às Cataratas de Cristal '
                                            f'por:\n₲{paises[15] * 640:.2f}.\033[m')
      else:
            print(cores[1], f'Você pode fazer um tour pelas missões jesuísticas '
                                            f'por:\n₲{paises[15]:.2f}\033[m')

if local.upper() == 'PERU':
      print(cores[1], f'Com seu dinheiro você pode comprar:\nS/{paises[17] * real:.2f} ')
      sleep(1)
      if real >= 218:
            print(f'Você pode ter uma experiência gastronômica com um chef em Mancora '
                  f'por:\nS/{paises[17] * 217.93:.2f}')
      else:
            print(f'Conheça Machupicchu com um guia por:\nS/{paises[17] * 216.55:.2f}')

if local.upper() == 'SURINAME':
      print(cores[1], f'Com seu dinheiro você pode '
                                      f'comprar:\n${paises[19] * real:.2f} Dolares do Suriname.')
      sleep(1)
      if real >= 550:
            print(f'Faça uma excursão pelas Ruines of Jodensavanne por:\n${paises[19] * 550:.2f}.\033[m')
      else:
            print(f'Faça uma City tour por:\n${paises[19] * 170:.2f}.\033[m')

if local.upper() == 'URUGUAI':
      sleep(1)
      print(cores[0], f'Com seu dinheiro você pode comprar:\n${paises[21] * real:.2f} '
                                  f'Pesos uruguaios.\033[m')
      sleep(1)
      if real >= 319:
            print(cores[0], f'Conheça a Colônia do Sacramento por:\n${paises[21] * 319:.2f}.\033[m')
      else:
            print(cores[0], f'Vá ao Pub Crawl Montevidéu, com valores à partir '
                                        f'de:\n${paises[21] * 109:.2f}.\033[m')

if local.upper() == 'VENEZUELA':
      print(cores[1], f'Com seu dinheiro você pode comprar:\n${paises[23] * real:.2f}')
