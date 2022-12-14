import main


def test_main(capsys):
    main.main()
    output, _ = capsys.readouterr()
    assert output == "Hello world.\n\n"
