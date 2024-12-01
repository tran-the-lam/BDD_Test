run_login_bdd:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd.py --us_path user-stories/login.txt --code_path login.py --prefix_output login
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --prefix_feature login --code_path login.py
	@echo "Step2: Complete steps file"
	@python scripts/generate_complete_step.py --prefix_output login --code_path login.py
	
