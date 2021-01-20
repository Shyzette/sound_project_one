while (true) {
    if (input.soundLevel() > 100 || input.temperature(TemperatureUnit.Fahrenheit) > 105) {
        light.setAll(light.rgb(255, 0, 0))
    }
    
    if (input.soundLevel() > 100 || input.temperature(TemperatureUnit.Fahrenheit) > 105) {
        music.pewPew.play()
    }
    
}
