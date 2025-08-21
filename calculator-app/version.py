import toml

def bump_version():
    data = toml.load("pyproject.toml")
    version = data["project"]["version"]
    
    major, minor, patch = map(int, version.split("."))
    patch += 1
    new_version = f"{major}.{minor}.{patch}"
    
    data["project"]["version"] = new_version
    with open("pyproject.toml", "w") as f:
        toml.dump(data, f)

    print(f"Version bumped: {version} → {new_version}")
    return new_version

if __name__ == "__main__":
    bump_version()
