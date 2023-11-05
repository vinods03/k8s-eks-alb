import json
import pickle
import numpy as np
from flask import Flask, request

model_name = 'car_price_rf_model.pkl'
car_price_model = pickle.load(open(model_name,'rb'))

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/health_check', methods = ['GET'])
@app.route('/car_price_predict/health_check', methods = ['GET'])
def health_checker(event = None, context = None):

    return "Health Check for car price app has completed successfully"

@app.route('/car_price_predict', methods = ['POST'])
def car_price_predictor(event = None, context = None):
    
        print('the model name is ', model_name)

        num_of_cylinders_two = 0
        num_of_cylinders_three = 0
        num_of_cylinders_four = 0
        num_of_cylinders_five = 0
        num_of_cylinders_six = 0
        num_of_cylinders_eight = 0
        num_of_cylinders_twelve = 0
    
        num_of_doors_two = 0
        num_of_doors_four = 0
    
        make_alfa_romero = 0
        make_audi = 0
        make_bmw = 0
        make_chevrolet = 0
        make_dodge = 0
        make_honda = 0
        make_isuzu = 0
        make_jaguar = 0
        make_mazda = 0
        make_mercedes_benz  = 0
        make_mercury = 0
        make_mitsubishi = 0
        make_nissan = 0
        make_peugot = 0
        make_plymouth = 0
        make_porsche = 0
        make_renault = 0
        make_saab = 0
        make_subaru = 0
        make_toyota = 0
        make_volkswagen = 0
        make_volvo = 0
    
        fuel_type_diesel = 0
        fuel_type_gas = 0
    
        aspiration_std = 0
        aspiration_turbo = 0
    
        engine_location_front = 0
        engine_location_rear = 0
    
        drive_wheels_4wd = 0
        drive_wheels_fwd = 0
        drive_wheels_rwd = 0
    
        body_style_convertible = 0
        body_style_hardtop = 0
        body_style_hatchback = 0
        body_style_sedan = 0
        body_style_wagon = 0
    
        engine_type_dohc = 0
        engine_type_l = 0
        engine_type_ohc = 0
        engine_type_ohcf = 0
        engine_type_ohcv = 0
        engine_type_rotor = 0
         
        fuel_system_1bbl = 0
        fuel_system_2bbl = 0
        fuel_system_4bbl = 0
        fuel_system_idi = 0
        fuel_system_mfi = 0
        fuel_system_mpfi = 0
        fuel_system_spdi = 0
        fuel_system_spfi = 0     
        
        data = request.get_json()
    
        symboling = data['symboling']
        normalized_losses = data['normalized-losses']
        wheel_base = data['wheel-base']
        length = data['length']
        width = data['width']
        height = data['height']
        curb_weight = data['curb-weight']
        engine_size = data['engine-size']
        bore = data['bore']
        stroke = data['stroke']
        compression_ratio = data['compression-ratio']
        horsepower = data['horsepower']
        peak_rpm = data['peak-rpm']
        city_mpg = data['city-mpg']
        highway_mpg = data['highway-mpg']
        make = data['make']
        fuel_type = data['fuel-type']
        aspiration = data['aspiration']
        num_of_doors = data['num-of-doors']
        body_style = data['body-style']
        drive_wheels = data['drive-wheels']
        engine_location = data['engine-location']
        engine_type = data['engine-type']
        num_of_cylinders = data['num-of-cylinders']
        fuel_system = data['fuel-system']       
                    
            
        if num_of_cylinders == 'two':
            num_of_cylinders_two = 1
        elif num_of_cylinders == 'three':
            num_of_cylinders_three = 1
        elif num_of_cylinders == 'four':
            num_of_cylinders_four = 1
        elif num_of_cylinders == 'five':
            num_of_cylinders_five = 1
        elif num_of_cylinders == 'six':
            num_of_cylinders_six = 1
        elif num_of_cylinders == 'eight':
            num_of_cylinders_eight = 1
        else:
            num_of_cylinders_twelve = 1
                
        if num_of_doors == 'two':
            num_of_doors_two = 1
        else:
            num_of_doors_foor = 1
                
        if make == 'alfa-romero':
            make_alfa_romero = 1
        elif make == 'audi':
            make_audi = 1
        elif make == 'bmw':
            make_bmw = 1
        elif make == 'chevrolet':
            make_chevrolet = 1
        elif make == 'dodge':
            make_dodge = 1
        elif make == 'honda':
            make_honda = 1
        elif make == 'isuzu':
            make_isuzu = 1
        elif make == 'jaguar':
            make_jaguar = 1
        elif make == 'mazda':
            make_mazda = 1
        elif make == 'mercedes_benz':
            make_mercedes_benz  = 1
        elif make == 'mercury':
            make_mercury = 1
        elif make == 'mitsubishi':
            make_mitsubishi = 1
        elif make == 'nissan':
            make_nissan = 1
        elif make == 'peugot':
            make_peugot = 1
        elif make == 'plymouth':
            make_plymouth = 1
        elif make == 'porsche':
            make_porsche = 1
        elif make == 'renault':
            make_renault = 1
        elif make == 'saab':
            make_saab = 1
        elif make == 'subaru':
            make_subaru = 1
        elif make == 'toyota':
            make_toyota = 1
        elif make == 'volkswagen':
            make_volkswagen = 1
        else:
            make_volvo = 1
                
        if aspiration == 'std':
            aspiration_std = 1
        else:
            aspiration_turbo = 1
                
        if body_style == 'convertible':
            body_style_convertible = 1
        elif body_style == 'hardtop':
            body_style_hardtop = 1
        elif body_style == 'hatchback':
            body_style_hatchback = 1
        elif body_style == 'sedan':
            body_style_sedan = 1
        else:
            body_style_wagon = 1
             
        if drive_wheels == '4wd':         
            drive_wheels_4wd = 1
        elif drive_wheels == 'fwd':
            drive_wheels_fwd = 1
        else:
            drive_wheels_rwd = 1
            
        if engine_type == 'dohc':
            engine_type_dohc = 1
        elif engine_type == 'l':
            engine_type_l = 1
        elif engine_type == 'ohc':
            engine_type_ohc = 1
        elif engine_type == 'ohcf':
            engine_type_ohcf = 1
        elif engine_type == 'ohcv':
            engine_type_ohcv = 1
        else:
            engine_type_rotor = 1
            
        if engine_location == 'front':
            engine_location_front = 1
        else:
            engine_location_rear = 1
            
        if fuel_system == '1bbl':
            fuel_system_1bbl = 1
        elif fuel_system == '2bbl':
            fuel_system_2bbl = 1
        elif fuel_system == '4bbl':
            fuel_system_4bbl = 1
        elif fuel_system == 'idi':
            fuel_system_idi = 1
        elif fuel_system == 'mfi':
            fuel_system_mfi = 1
        elif fuel_system == 'mpfi':
            fuel_system_mpfi = 1
        elif fuel_system == 'spdi':
            fuel_system_spdi = 1
        else:
            fuel_system_spfi = 1      
                        
        if fuel_type == 'diesel':
            fuel_type_diesel = 1
        else:
            fuel_type_gas = 1
                
            
        input_to_model = np.array([[
            symboling,
            normalized_losses,
            wheel_base,
            length,
            width,
            height,
            curb_weight,
            engine_size,
            bore,
            stroke,
            compression_ratio,
            horsepower,
            peak_rpm,
            city_mpg,
            highway_mpg,
            make_alfa_romero,
            make_audi,
            make_bmw,
            make_chevrolet,
            make_dodge,
            make_honda,
            make_isuzu,
            make_jaguar,
            make_mazda,
            make_mercedes_benz,
            make_mercury,
            make_mitsubishi,
            make_nissan,
            make_peugot,
            make_plymouth,
            make_porsche,
            make_renault,
            make_saab,
            make_subaru,
            make_toyota,
            make_volkswagen,
            make_volvo,
            fuel_type_diesel,
            fuel_type_gas,
            aspiration_std,
            aspiration_turbo,
            num_of_doors_four,
            num_of_doors_two,
            body_style_convertible,
            body_style_hardtop,
            body_style_hatchback,
            body_style_sedan,
            body_style_wagon,
            drive_wheels_4wd,
            drive_wheels_fwd,
            drive_wheels_rwd,
            engine_location_front,
            engine_location_rear,
            engine_type_dohc,
            engine_type_l,
            engine_type_ohc,
            engine_type_ohcf,
            engine_type_ohcv,
            engine_type_rotor,
            num_of_cylinders_eight,
            num_of_cylinders_five,
            num_of_cylinders_four,
            num_of_cylinders_six,
            num_of_cylinders_three,
            num_of_cylinders_twelve,
            num_of_cylinders_two,
            fuel_system_1bbl,
            fuel_system_2bbl,
            fuel_system_4bbl,
            fuel_system_idi,
            fuel_system_mfi,
            fuel_system_mpfi,
            fuel_system_spdi,
            fuel_system_spfi
            ]])
            
        print('input_to_model is ', input_to_model)
            
        car_price = car_price_model.predict(input_to_model)
        
        return str(car_price)
            
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
        

        

        

            
    
