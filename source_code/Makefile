gen_steps_of_file:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd.py --task $(task)
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --task $(task)	
	@echo "Step3: Complete steps file"
	@python scripts/generate_complete_step.py --task $(task)

gen_steps_of_folder:
	@echo "Step1: Generate BDD"
	@python scripts/generate_bdd_of_folder.py --task $(task)
	@echo "Step2: Generate steps file"
	@python scripts/generate_step_definition.py --task $(task)	
	@echo "Step3: Complete steps file"
	@python scripts/generate_complete_step_of_folder.py --task $(task)