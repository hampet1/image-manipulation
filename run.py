from app import app

print("root path is", app.root_path)

if __name__ == "__main__":
    app.run(debug=True)