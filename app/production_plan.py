def calculate_production_plan(payload):
    try:
        # Calculate wind power
        wind_power = payload["load"] * (payload["fuels"]["wind(%)"] / 100)

        # Sort power plants
        powerplants = sorted(
            [
                plant
                for plant in payload["powerplants"]
                if plant["type"] in ["gasfired", "turbojet"]
            ],
            key=lambda x: x["efficiency"],
        )

        # Add wind turbines to the end of the sorted list
        powerplants.extend(
            [
                plant
                for plant in payload["powerplants"]
                if plant["type"] == "windturbine"
            ]
        )

        # Calculate power output
        production_plan = []
        remaining_load = payload["load"] - wind_power

        for plant in powerplants:
            pmin = plant["pmin"]
            pmax = plant["pmax"]
            efficiency = plant["efficiency"]

            # Calculate power output for gas-fired and turbojet power plants
            if plant["type"] in ["gasfired", "turbojet"]:
                p = min(
                    max(
                        remaining_load
                        * efficiency
                        / (1 - wind_power / payload["load"]),
                        pmin,
                    ),
                    pmax,
                )
            else:
                # For wind turbines, the efficiency is not applicable
                p = min(max(remaining_load, pmin), pmax)

            # Ensure power is a multiple of 0.1 MW
            p = round(p / 0.1) * 0.1

            production_plan.append({"name": plant["name"], "p": round(p, 2)})

            remaining_load -= p
        # Create response
        return production_plan
    
    except Exception as e:
        raise RuntimeError(f"Error in the calculate_production_plan method: {str(e)}")
