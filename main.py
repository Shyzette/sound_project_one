while True:
    if input.sound_level() > 100 or input.temperature(TemperatureUnit.FAHRENHEIT) >105:
        light.set_all(light.rgb(0,0,255))

    if input.sound_level() > 100 or input.temperature(TemperatureUnit.FAHRENHEIT) >105:
        music.pew_pew.play_until_done()




