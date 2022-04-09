import nltk
nltk.download('punkt')

caliberlist = [".17 Aguila",".17 Fireball",".17 Hornady Magnum Rimfire (HMR)",".17 Mach 2",".17 Remington",".204 Ruger",".218 Bee",".22 Hornet",".22 Long",".22 Long Rifle High Velocity and Hyper Velocity",".22 Rimfire Shotshells",".22 Short",".22 Standard Velocity and Match Ammunition",".22 Winchester Magnum Rimfire",".22-250 Remington",".220 Swift",".221 Remington Fireball",".222 Remington",".222 Remington Magnum",".223 Remington",".223 Winchester Super Short Magnum (WSSM)",".224 Weatherby Magnum",".225 Winchester",".240 Weatherby Magnum",".243 Winchester",".243 Winchester Super Short Magnum",".25 Auto (ACP)",".25 Winchester Super Short Magnum (WSSM)",".25-06 Remington",".25-20 Winchester",".25-35 Winchester",".250 Savage",".257 Roberts",".257 Weatherby Magnum",".260 Remington",".264 Winchester Magnum",".270 Weatherby Magnum",".270 Winchester",".270 Winchester Short Magnum",".280 Remington",".284 Winchester",".30 Luger (7.65mm)",".30 M1 Carbine",".30-06 Springfield",".30-30 Winchester",".30-378 Weatherby",".300 Dakota",".300 H&H Magnum",".300 Remington Short Action Ultra Magnum",".300 Remington Ultra Magnum",".300 Savage",".300 Weatherby Magnum",".300 Winchester Magnum",".300 Winchester Short Magnum",".303 British",".307 Winchester",".308 Winchester (7.62mm NATO)",".32 Auto (7.65mm Browning)",".32 H&R Magnum",".32 Short Colt",".32 Smith & Wesson",".32 Smith & Wesson Long",".32 Winchester Special",".32-20 Winchester",".325 Winchester Short Magnum",".327 Federal Magnum",".330 Dakota",".338 A Square",".338 Lapua Magnum",".338 Remington Ultra Magnum",".338 Winchester Magnum",".338-378 Weatherby",".340 Weatherby Magnum",".35 Remington",".35 Whelen",".350 Remington Magnum",".356 Winchester",".357 Magnum",".357 Magnum (Rifle Data)",".357 SIG",".375 A-Square",".375 Dakota",".375 Holland & Holland Magnum",".375 Remington Ultra Magnum",".375 Ruger",".375 Weatherby Magnum",".375 Winchester",".378 Weatherby Magnum",".38 Short Colt",".38 Smith & Wesson",".38 Special (.38 Smith & Wesson Special)",".38 Super Auto Colt",".38-40 Winchester",".38-55 Winchester",".380 Auto (9mm Browning Short)",".40 Smith & Wesson",".400 A-Square Dual Purpose Magnum (DPM)",".404 Dakota",".405 Winchester",".41 Remington Magnum",".416 Dakota",".416 Remington Magnum",".416 Rigby",".416 Weatherby Magnum",".44 Colt",".44 Remington Magnum (Pistol Data)",".44 Remington Magnum (Rifle Data)",".44 Smith & Wesson Special",".44-40 Winchester",".444 Marlin",".45 Auto (.45 ACP)",".45 Colt (.45 Long Colt)",".45 GAP (Glock Automatic Pistol)",".45 Smith & Wesson Schofield",".45 Winchester Magnum",".45-70 Government",".450 Dakota",".450 Marlin",".454 Casull",".458 Lott",".458 Winchester Magnum",".460 Smith & Wesson",".460 Weatherby Magnum",".470 Nitro Express",".475 Linebaugh",".475 Nitro Express Number 2",".480 Ruger",".495 A-Square",".50 Action Express",".500 A-Square",".500 Jeffery",".500 Nitro Express 3-Inch",".500 Smith & Wesson Special",".500 Smith & Wesson Special Magnum",".500-465 Nitro Express",".505 Rimless Magnum (Gibbs)",".577 Nitro Express 3-Inch",".577 Tyrannosaur",".600 Nitro Express",".700 Nitro Express","10.57mm (.416) Lazzeroni Meteor","10mm Auto","5mm Remington Rimfire Magnum","6.17mm (.243) Lazzeroni Spitfire","6.5 Mannlicher-Schoenauer","6.53mm (.257) Lazzeroni Scramjet","6.5mm Remington Magnum","6.5x55mm Swedish Mauser","6.5x57 Mauser","6.71mm (.264) Lazzeroni Phantom","6.8mm Remington SPC","6mm Remington","7-30 Waters","7.21mm (.284) Lazzeroni Firebird","7.62x39mm Russian","7.82mm (.308) Lazzeroni Patriot","7.82mm (.308) Lazzeroni Warbird","7mm Dakota","7mm Remington Magnum","7mm Remington Short Action Ultra Magnum","7mm Remington Ultra Magnum","7mm STW (Shooting Times Westerner)","7mm Weatherby Magnum","7mm Winchester Short Magnum (WSM)","7mm-08 Remington","7x57mm Mauser","7x64mm Brenneke","8.59mm (.338) Lazzeroni Titan","8mm Remington Magnum","8x57mm Mauser JS","9.3x74R","9mm Largo (9x23mm)","9mm Luger (9mm Parabellum) (9x19mm)","9mm Makarov (9x18mm)","9x23mm Winchester"]
gc_list = ['.450 Rigby', '357 Super Magnum', '.250-3000 Savage', '44 Henry Rimfire', '7.62mm Caliber']

title_index = 0
result = []
for title in gc_list:
    # print('nltk.word_tokenize(title)')
    # print(nltk.word_tokenize(title))
    min = nltk.edit_distance(title, caliberlist[0])
    prev = 0
    list = []
    for ary in caliberlist:
        # print('nltk.word_tokenize(ary)')
        # print(nltk.word_tokenize(ary))
        # print(title)
        # print(ary)
        print(nltk.edit_distance(title, ary))
        recent = nltk.edit_distance(title, ary)
        if recent < min:
            min = recent
            list = {title, ary}
    print('min')
    print(list)
    print(min)
    result.append(list)
print(result)    
