import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')

def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")

def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
        metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))

    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])

    if 'config' in metafunc.fixturenames:
        metafunc.parametrize("config", [json.loads('{"port":3000,"address":"https://d2eb7802-3c91-466b-bd39-6327eb475ea0.ws-us02.gitpod.io","editor":"gitpod","configPath":{"config":"bc.json","base":".learn","exercises":"./exercises","output":".learn/dist"},"outputPath":"./.learn/dist","publicPath":"/preview","grading":"isolated","ignoreRegex":null,"webpack_template":null,"disable_grading":false,"onCompilerSuccess":null,"language":"python3","compiler":"python3","tester":"pytest","actions":["run","test","reset"],"title":"Learn Python Interactively (beginner)","repository":"https://github.com/4GeeksAcademy/python-beginner-programming-exercises","preview":"https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/master/preview.png?raw=true","description":"Python Exercises for beginners, from Hello World to variables, loops and a little bit of functions","duration":10,"difficulty":"easy","video-solutions":true,"graded":true,"session":3203907720544607700,"exercises":[{"slug":"00-Welcome","title":"00-Welcome","done":false,"path":"exercises/00-Welcome","translations":["es","us"],"graded":false},{"slug":"01-Console","title":"01-Console","done":true,"path":"exercises/01-Console","translations":["es","us"],"graded":true},{"slug":"02-Declare-Variables","title":"02-Declare-Variables","done":true,"path":"exercises/02-Declare-Variables","translations":["es","us"],"graded":true},{"slug":"03-Print-Variables-In-The-Console","title":"03-Print-Variables-In-The-Console","done":true,"path":"exercises/03-Print-Variables-In-The-Console","translations":["es","us"],"graded":true},{"slug":"04-Multiply-Two-Values","title":"04-Multiply-Two-Values","done":true,"path":"exercises/04-Multiply-Two-Values","translations":["es","us"],"graded":true},{"slug":"05-User-Inputed-Values","title":"05-User-Inputed-Values","done":true,"path":"exercises/05-User-Inputed-Values","translations":["es","us"],"graded":true},{"slug":"06-String-Concatenation","title":"06-String-Concatenation","done":true,"path":"exercises/06-String-Concatenation","translations":["es","us"],"graded":true},{"slug":"07-Create-a-Basic-HTML","title":"07-Create-a-Basic-HTML","done":true,"path":"exercises/07-Create-a-Basic-HTML","translations":["es","us"],"graded":true},{"slug":"08-Your-First-If","title":"08-Your-First-If","done":true,"path":"exercises/08-Your-First-If","translations":["es","us"],"graded":true},{"slug":"08.1-How-Much-The-Wedding-Costs","title":"08.1-How-Much-The-Wedding-Costs","done":true,"path":"exercises/08.1-How-Much-The-Wedding-Costs","translations":["es","us"],"graded":true},{"slug":"09-Random-Numbers","title":"09-Random-Numbers","done":true,"path":"exercises/09-Random-Numbers","translations":["es","us"],"graded":true},{"slug":"10-Calling-Your-First-Function","title":"10-Calling-Your-First-Function","done":true,"path":"exercises/10-Calling-Your-First-Function","translations":["es","us"],"graded":true},{"slug":"10.01-Creating-Your-First-Function","title":"10.01-Creating-Your-First-Function","done":true,"path":"exercises/10.01-Creating-Your-First-Function","translations":["es","us"],"graded":true},{"slug":"11-Create-A-New-Function","title":"11-Create-A-New-Function","done":false,"path":"exercises/11-Create-A-New-Function","translations":["es","us"],"graded":true},{"slug":"14-Rand-From-One-to-Six","title":"14-Rand-From-One-to-Six","done":false,"path":"exercises/14-Rand-From-One-to-Six","translations":["es","us"],"graded":true},{"slug":"15-Your-First-Loop","title":"15-Your-First-Loop","done":true,"path":"exercises/15-Your-First-Loop","translations":["es","us"],"graded":true},{"slug":"16-Create-A-For-Loop","title":"16-Create-A-For-Loop","done":false,"path":"exercises/16-Create-A-For-Loop","translations":["es","us"],"graded":true},{"slug":"18-Random-Colors-Loop","title":"18-Random-Colors-Loop","done":false,"path":"exercises/18-Random-Colors-Loop","translations":["es","us"],"graded":true},{"slug":"19-Looping-With-FizzBuzz","title":"19-Looping-With-FizzBuzz","done":false,"path":"exercises/19-Looping-With-FizzBuzz","translations":["es","us"],"graded":true},{"slug":"20-Russian-Roulette","title":"20-Russian-Roulette","done":false,"path":"exercises/20-Russian-Roulette","translations":["es","us"],"graded":true},{"slug":"21-The-Beatles","title":"21-The-Beatles","done":false,"path":"exercises/21-The-Beatles","translations":["es","us"],"graded":true},{"slug":"22-Bottles-Of-Milk","title":"22-Bottles-Of-Milk","done":false,"path":"exercises/22-Bottles-Of-Milk","translations":["es","us"],"graded":true}]}')])
