import os
from pathlib import Path
import shutil
import sys
import subprocess
from subprocess import PIPE, Popen

# Check if we're in a git repo
try:
    repo_dir = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, check=True).stdout.decode().strip()
    repo = Path(repo_dir).name
except subprocess.CalledProcessError:
    repo = os.environ.get("FSDL_REPO", "fsdl-text-recognizer-2022-labs")

branch = os.environ.get("FSDL_BRANCH", "main")
token = os.environ.get("FSDL_GHTOKEN")
prefix = token + "@" if token else ""

in_colab = "google.colab" in sys.modules

def _go():
    if in_colab: # Create the repo and cd into it
        repo_root = Path("/") / "content" / repo
        os.chdir(repo_root.parent)
        
        shutil.rmtree(repo_root, ignore_errors=True)
        _clone_repo(branch, prefix)
            
        os.chdir(repo_root)

        _install_dependencies_colab()

    else: # Move to the repo root
        os.chdir(repo_dir)
        
        
def change_to_lab_dir(lab_idx=None):
    if lab_idx is None:
        return
    
    if not repo.endswith("labs"):
        return  # This is only needed in the labs repo

    lab_name = f"lab{str(lab_idx).zfill(2)}"
    cwd = Path.cwd().name
    if cwd!= lab_name:  # If we're not in the lab directory
        if cwd!= repo:  # Check that we're in the repo root
            raise RuntimeError(f"run this command from the root of repo {repo}, not {cwd}")
        os.chdir(lab_name)  # And then cd into the lab directory


def _clone_repo(branch, prefix):
    # Directly specify the URL to your repository
    url = f"https://{prefix}github.com/ruchithareddy269/258-Deep_learning-Project"
    subprocess.run(  # Run git clone
        ["git", "clone", "--branch", branch, "-q", url], check=True)


def _install_dependencies_colab():
    subprocess.run( # Directly pip install the prod requirements
        ["pip", "install", "--quiet", "-r", "requirements/prod.in"], check=True)

    # Run a series of commands with pipes to pip install the dev requirements
    subprocess.run(
        ["sed 1d requirements/dev.in | grep -v '#' | xargs pip install --quiet"],
        shell=True, check=True)
        
    # Reset pkg_resources list of requirements so gradio can infer its version correctly
    import pkg_resources
    
    pkg_resources._initialize_master_working_set()


_go()
