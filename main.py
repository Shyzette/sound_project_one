while True:
    if input.sound_level() > 100 or input.temperature(TemperatureUnit.FAHRENHEIT) >105:
        light.set_all(light.rgb(255,0,0))

    if input.sound_level() > 100 or input.temperature(TemperatureUnit.FAHRENHEIT) >105:
        music.pew_pew.play()




