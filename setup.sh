
#TODO remove 
sudo apt update && sudo apt install screen 
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
uv pip install --upgrade git+https://github.com/huggingface/transformers.git 


# install and build llama cpp 
bash setup_llamacpp.sh


# install invokeai
cd .. 
deactivate 
git clone https://github.com/MubaslatLaith/InvokeAI-CanvasDirector.git
git clone https://github.com/MubaslatLaith/invokeai.git
cd InvokeAI-CanvasDirector
bash setup.sh




