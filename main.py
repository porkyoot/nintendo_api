
import sys, animal_crossing as ac

def main() -> int:
    tokens = ac.login()
    ac.send('Spoon', tokens=tokens)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit