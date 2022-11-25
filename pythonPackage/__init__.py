#
from pythonPackage import getData
# Take dict as input



if __name__ == '__main__':
    print('#################### Welcome to python world ##########################')
    # storing input dictionary
    data = {}
    userWantToInput = 'y'
    while True:
        key = str(input('Enter key : '))
        value = str(input('Enter Value: '))
        data[key] = value

        userWantToInput = input('Do you have more pairs to insert ? [Y/N]: ')
        while userWantToInput not in ['y', 'n', 'Y', 'N']:
            userWantToInput = input('Please Enter Y or N ? [Y/N]: ')
        if userWantToInput.upper() == 'Y':
            continue
        else:
            break
    print('Your Data saved successfully !!')

    print('################################################')

    # keys for that values we want to fetch
    keys = []

    while True:
        keys.append(str(input('Enter Key: ')))
        doyouHaveMoreToadd = str(input('Do you want to add more key ? [Y/N]: '))
        while doyouHaveMoreToadd not in ['y', 'n', 'Y', 'N']:
            doyouHaveMoreToadd = input('Please Enter Y or N  [Y/N]: ')
        if doyouHaveMoreToadd.upper() == 'Y':
            continue
        else:
            break

    print('################################################')

    print('Your requested data is as follows:  ')
    req_data = getData.getRequiredData(keys , data )
    if len(req_data) == 0:
        print('Oops no matching key available !! ')
    else:
        print(req_data)

