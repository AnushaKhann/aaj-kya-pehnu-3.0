import platform

import torch


def print_system_info():

    print("=" * 60)

    print("Operating System :", platform.system())

    print("Machine          :", platform.machine())

    print("Python           :", platform.python_version())

    print("PyTorch          :", torch.__version__)

    print("MPS Available    :", torch.backends.mps.is_available())

    print("=" * 60)