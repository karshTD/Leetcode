class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x [1] , reverse = True)

        total_units = 0
        remaining = truckSize

        for boxes, units in boxTypes:
            if boxes <= remaining:
                total_units += boxes * units
                remaining -= boxes
            else:
                total_units += remaining * units
                break
    
        return total_units

