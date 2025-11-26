def convert_to_celsuis():
    try:
        num = float(input("Enter temperature in Fareinheit: "))
        converted_num = (num - 32) * 5/9
    except ValueError:
        print("Please enter numbers only")
    else:
        print(f"Temperature in celsuis: {converted_num:.2f}")
    finally:
        print("Conversion complete.")

convert_to_celsuis()