let mano = 0
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.SmallSquare)
})
input.onGesture(Gesture.Shake, function () {
    mano = randint(0, 2)
    if (mano == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (mano == 1) {
        basic.showIcon(IconNames.Square)
    } else if (mano == 2) {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Scissors)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Square)
})
