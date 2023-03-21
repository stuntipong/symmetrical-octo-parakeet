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