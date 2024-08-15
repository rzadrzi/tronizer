
import os
import sys

sys.path.append(os.path.join(os.getcwd(), "app"))

# Web module
sys.path.append(os.path.join(os.getcwd(), "app", "web"))
# modules inside Web module
sys.path.append(os.path.join(os.getcwd(), "app", "web", "controllers"))
sys.path.append(os.path.join(os.getcwd(), "app", "web", "database"))
sys.path.append(os.path.join(os.getcwd(), "app", "web", "models"))
sys.path.append(os.path.join(os.getcwd(), "app", "web", "routes"))
sys.path.append(os.path.join(os.getcwd(), "app", "web", "schema"))
# Coins module
sys.path.append(os.path.join(os.getcwd(), "app", "coins"))
# modules inside Coins module
sys.path.append(os.path.join(os.getcwd(), "app", "coins", "tron"))


sys.path.append(os.path.join(os.getcwd(), "app", "scheduler"))
sys.path.append(os.path.join(os.getcwd(), "app", "scheduler", "tasks"))


sys.path.append(os.path.join(os.getcwd(), "app", "web", "templates"))
sys.path.append(os.path.join(os.getcwd(), "app", "web", "templates", "static"))


print(sys.path)