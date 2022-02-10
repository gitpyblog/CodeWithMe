def dodawanie(a,b):
    return a + b

print(dodawanie(2,3))

def test_dodawanie():
    # given
    par_a = 2
    par_b = 3

    # when
    result = dodawanie(par_a, par_b)

    # then
    assert result == 6



