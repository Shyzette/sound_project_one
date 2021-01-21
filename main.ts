while (true) {
    if (input.soundLevel() > 100 || input.temperature(TemperatureUnit.Fahrenheit) > 105) {
        light.setAll(light.rgb(0, 0, 255)) && music.pewPew.playUntilDone()
    }
    
}
