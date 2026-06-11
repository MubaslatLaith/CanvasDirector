
#TODO remove 
mv /workspace/invokeai /workspace/invokeai_preexsiting 

pip3 install virtualenv
#git setup
git config --global user.name "MubaslatLaith"
git config --global user.email "laithmbt@gmail.com"
git config --global credential.helper store
git init

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel

pip install poetry
poetry env use $(pwd)/.venv/bin/python
poetry install
poetry run playwright install chromium
poetry run playwright install-deps chromium


cd .. 

deactivate 
git clone https://github.com/MubaslatLaith/InvokeAI-ContextManager.git
git clone https://github.com/MubaslatLaith/invokeai.git
cd InvokeAI-ContextManager
bash setup.sh




