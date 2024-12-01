gen_steps_file:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd.py --task $(task)
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --task $(task)	
	@echo "Step3: Complete steps file"
	@python scripts/generate_complete_step.py --task $(task)


run_login_bdd:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd.py --task login
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --task login
	@echo "Step3: Complete steps file"
	@python scripts/generate_complete_step.py --task login

run_hrm_bdd:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd.py --task hrm
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --task hrm
	@echo "Step3: Complete steps file"
	@python scripts/generate_complete_step.py --task hrm

