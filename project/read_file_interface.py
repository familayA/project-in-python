from abc import ABC, abstractmethod
class ReadFile(ABC):
   @abstractmethod
   def read_file(self,file_path:str):
       pass
