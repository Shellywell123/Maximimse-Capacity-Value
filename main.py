
def maxDuffelBagValue(cakes, capacity):
    """
    """  
    results = []
    combs = []

    for i in range(0,len(cakes)):
        cake = cakes[i]
        comb_str = ''
        total_value = 0
        remainder = capacity%cake['weight']
        max_cakes =(capacity - remainder)/cake['weight']
        max_weight = max_cakes*cake['weight']
        max_value = max_cakes*cake['pounds']
        free_space = capacity-max_weight
        total_value = total_value + max_value
        comb_str += str(int(max_cakes))+'x'+str(i)+'-'
      #  print('£'+str(total_value),comb_str)
        results.append(total_value)
        combs.append(comb_str)

        if free_space > 0:
            for j in range(0,len(cakes)):
                cake = cakes[j]
                remainder = free_space%cake['weight']
                max_cakes =(free_space - remainder)/cake['weight']
                max_weight = max_cakes*cake['weight']
                max_value = max_cakes*cake['pounds']
                total_value = total_value + max_value
                subfree_space = free_space-max_weight
                comb_str += str(int(max_cakes))+'x'+str(j)+'-'
              #  print('£'+str(total_value),(comb_str)   )
                results.append(total_value)
                combs.append(comb_str)

    max_haul  = max(results)
    haul_comb = combs[results.index(max(results))]
    print('£'+str(max_haul),haul_comb)
    return max_haul,haul_comb

#using the supplied example

cakes = [{ 'name':'a','weight':7, 'pounds': 160 }, { 'name':'b','weight': 3, 'pounds': 90 }, { 'name':'c','weight': 2, 'pounds': 15}]
capacity = 20
maxDuffelBagValue(cakes, capacity)