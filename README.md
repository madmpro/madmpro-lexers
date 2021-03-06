# madmpro-lexers
A package created to add additional lexers for use in Pygments.

# Included Lexers

| Lexers | Description |
|-------|-------------|
| bsl | Simple lexer for Language 1C. |

## Adding New Lexers
To add a new lexer, the lexer must be dropped into the `madmpro-lexers` folder.  The `__init__.py` file must be updated to expose the lexer.  Lastly, `setup.py` must be modified to setup the entry points for the new lexer.

## Install

    $ git clone https://github.com/madmpro/madmpro-lexers.git
    $ cd madmpro-lexers
    $ (sudo) python setup.py install

### Verify

Verify that the package installed correctly by looking for the lexer "bsl" in the output of

    $ pygmentize -L lexers | grep bsl

Based on projects:
- https://github.com/facelessuser/pymdown-lexers
- https://github.com/zurapa/Lang1CLexer
- https://jenyay.net/Outwiker/SourcePlugin
- [Jenyay/outwiker](https://github.com/Jenyay/outwiker/blob/62d310dbf0c8b8067bb9b04ae9c68833be57d1ea/plugins/source/source/pygments/lexers/1S.py#L42)
