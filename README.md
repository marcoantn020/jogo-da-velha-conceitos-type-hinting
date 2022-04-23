### Jogo da velha 
- aplicando conceitos de type hinting
- utilizando biblioteca mypy para checar tipagem

**rodando game**

    - crie um ambiente virtual
        - virtualenv --python=python3 game
    
    - ativar ambiente virtual
        - source game/bin/active

    - instale a biblioteca mypy e flake8
        - pip install mypy
        - pip install flake8

    - checar as tipagens
        - mypy game.py
    
    - checar padrão pep8
        - flake game.py
    
    - rodar game
        - python game.py

**opção sem ambiente virtual**

    - instale o pacote mypy
        - pip install -r requirements.txt

    - checar tipagens
        - mypy game.py
        
    - rodar game
        - python3 game.py
