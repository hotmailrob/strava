PROJECT=strava-api

conda-env:
	conda env remove --name $(PROJECT) --yes 2>/dev/null || true
	conda env create --name $(PROJECT) --file envs/environment.yml
	conda run --name $(PROJECT) pip install -e