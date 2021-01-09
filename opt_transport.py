from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, PULP_CBC_CMD
import numpy as np

# Store the key figures
hardware = ["Notebook Büro 13\"", "Notebook Büro 14\"", "Notebook outdoor", "Mobiltelefon Büro", "Mobiltelefon Outdoor",
            "Mobiltelefon Heavy Duty", "Tablet Büro klein", "Tablet Büro groß", "Tablet outdoor klein", "Tablet outdoor groß"]
max_amount = [205, 420, 450, 60, 157, 220, 620, 250, 540, 370]
weights = [2451, 2978, 3625, 717, 988, 1220, 1405, 1455, 1690, 1980]
benefits = [40, 35, 80, 30, 60, 65, 40, 40, 45, 68]

# Create the model
model = LpProblem(name="opt-transport", sense=LpMaximize)

# Initialize the decision variables
x = list({i: LpVariable(name=f"x{i}", lowBound=0, cat="Integer") for i in range(1, 21)}.values())

# Add the constraints to the model
total_weight1 = np.dot(weights, x[:10])
total_weight2 = np.dot(weights, x[10:])
model += (total_weight1 <= 1100000 - 72400, "transporter1")             # Upper limit for the loading weight of the first transporter
model += (total_weight2 <= 1100000 - 85700, "transporter2")             # Upper limit for the loading weight of the second transporter
for i in range(10):
    model += (x[i] + x[i+10] <= max_amount[i], f"max_amount{i}")        # Upper limits for the maximum number of units

# Add the objective function to the model
model += lpSum([np.dot(benefits, x[:10]), np.dot(benefits, x[10:])])    # Maximize the total benefit

# Solve the problem; The relative gap tolerance (gapRel) is used as the termination criterion.
status = model.solve(PULP_CBC_CMD(gapRel =0.0002))

if model.status:
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"Total benefit: {model.objective.value()}\n")

    # TODO: mehr Infos anzeigen
    # - Gesamtgewicht je Transporter
    # - Freies Gewicht

    # for var in model.variables():
    #     print(f"{var.name}: {var.value()}")

    # for name, constraint in model.constraints.items():
    #     print(f"{name}: {constraint.value()}")

    for i in range (10):
        opt_amount = x[i].value() + x[i+10].value()
        print(f"\t{hardware[i]}: {opt_amount}")

    for j in range(2):
        print(f"\nTransporter {j+1}:")
        for i in range(10):
            print(f"\t{hardware[i]}: {x[i + j * 10].value()}")
        
        ls = [type(item) for item in x[:10]]
        print(ls)
        #total_weight = (np.dot(weights, list(x.values())[:10]) + (j % 2) * 72400 + (j % 2) * 85700) / 1000
        #print(f"\t=> total loading weight in kilograms (incl. driver): {total_weight}")

else:
    print("The optimum could not be determined.")
