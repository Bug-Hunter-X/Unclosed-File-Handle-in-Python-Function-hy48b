def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write('This is some text.')
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception appropriately

#Alternative way:
def function_with_explicit_close(filename):
    f = open(filename, 'w')
    try:
        # ... some code that might raise an exception ...
        f.write('This is some text.')
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception appropriately
    finally:
        f.close() # Ensure file is always closed