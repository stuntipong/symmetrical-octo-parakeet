import sky_sim
from numpy import testing

def test_module_import():
    try:
        import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return

if __name__ == "__main__":
    # introspect and run all the functions starting with 'test'
    for f in dir():
        if f.startswith('test'):
            print(f)
            globals()[f]()
            
def test_get_radec():
    answer = (14.215420962967535, 41.26916666666667)
    result = sky_sim.get_radec()
    testing.assert_allclose(answer, result, atol=1./3600) #add some more tolerance in the test
    return
    #if answer != result:
    #    raise AssertionError(f"Position of M31 Should be {answer}, but got {result}")