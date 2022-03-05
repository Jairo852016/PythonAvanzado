#Hola 3-> HolaHolaHola


def make_division_by(n):
    def division_by(d):
        return d/n
    return division_by


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater

def run():
    repeate_5= make_repeater_of(5)
    print(repeate_5("Hola"))
    repeate_10= make_repeater_of(10)
    print(repeate_10("Jairo"))
    division_by_3=make_division_by(3)
    print(division_by_3(18))
    division_by_5=make_division_by(5)
    print(division_by_5(100))


if __name__ =="__main__":
    run()