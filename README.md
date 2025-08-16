# uv_project_setup
faster than pip & venv combined → [uv](https://docs.astral.sh/uv/#highlights)

1. ```pip install uv```
2. ```uv init '{project_name}'``` OR ```uv init``` (for current dir)
3. ```uv venv```
4. ```.venv/Scripts/activate```
5. ```uv add numpy```
6. ```uv add -r requirements.txt```
7. ```uv run main.py```
8. ```uv sync``` → to sync all the pkgs.
9. ```uv lock``` → to lock all the pkgs.
10. ```uv tree``` (dependencies)



mac/linux: ```pip freeze > requirements.txt```