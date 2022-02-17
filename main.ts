input.onButtonPressed(Button.B, function () {
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Forward, 56)
})
kitronik_servo_lite.turnLeft(0)
kitronik_servo_lite.right()
