def on_button_pressed_b():
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
        kitronik_motor_driver.MotorDirection.FORWARD,
        56)
input.on_button_pressed(Button.B, on_button_pressed_b)

kitronik_servo_lite.turn_left(0)
kitronik_servo_lite.right()
KitronikRoboticsBoard.motorOn(KitronikRoboticsBoard, 2, "forward", 10)
