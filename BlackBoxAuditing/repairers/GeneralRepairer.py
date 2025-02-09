from BlackBoxAuditing.repairers.AbstractRepairer import AbstractRepairer
from BlackBoxAuditing.repairers.CategoricRepairer import Repairer as CategoricRepairer
from BlackBoxAuditing.repairers.NumericRepairer import Repairer as NumericRepairer

class Repairer(AbstractRepairer):
  def __init__(self, *args, **kwargs):
    super(Repairer, self).__init__(*args, **kwargs)
    print("Working")
    if self.kdd:
        print("KDD")
        self.repairer = CategoricRepairer(*args,**kwargs)
    else:
        if all(isinstance(row[self.feature_to_repair],float) for row in self.all_data):
          self.repairer = NumericRepairer(*args, **kwargs)
          print("Float_Numeric")
        elif all(isinstance(row[self.feature_to_repair],int) for row in self.all_data):
          self.repairer = NumericRepairer(*args, **kwargs)
          print("Int_Numeric")
        elif all(isinstance(row[self.feature_to_repair],str) for row in self.all_data):
          self.repairer = CategoricRepairer(*args, **kwargs)
          print("Categoric")

  def repair(self, data_to_repair):
    return self.repairer.repair(data_to_repair)
