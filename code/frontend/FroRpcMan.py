import grpc

from proto import Managment_pb2
from proto import Managment_pb2_grpc



ADDR_PORT = 'management:50052'




class AdditionalServices:
    def __init__(self, bagaglioSpeciale, bagaglioStivaMedio, bagaglioStivaGrande, assicurazioneBagagli, animaleDomestico, neonato):
        self.bagaglioStivaMedio = bagaglioStivaMedio
        self.animaleDomestico = animaleDomestico
        self.assicurazioneBagagli = assicurazioneBagagli
        self.bagaglioStivaGrande = bagaglioStivaGrande
        self.bagaglioSpeciale = bagaglioSpeciale
        self.neonato = neonato




class SeatsFlight:
    def __init__(self, primo, secondo, terzo, quarto, quinto):
        self.primo = primo
        self.secondo = secondo
        self.terzo = terzo
        self.quarto = quarto
        self.quinto = quinto




def sendIdCompanySeatsPrice(compagnia):
    # Apertura di un gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    # Creazione del client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    output = []
    # Ottengo uno stream di messaggio da parte del Server
    for entry in stub.GetAllSeatsFlight(Managment_pb2.SeatCostRequest(compagnia=compagnia)):
        #print(entry.prezzo)
        output.append(entry.prezzo)
    
    """
    output[0] = primo
    output[1] = secondo
    output[2] = terzo
    output[3] = quarto
    output[4] = quinto   
    """
    
    seatsFlight = SeatsFlight(output[0], output[1], output[2], output[3], output[4])
    return seatsFlight




def sendIdCompanyAdditionalService(compagnia):

    # Apertura di un gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    # Creazione del client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    output = []
    # Ottengo uno stream di messaggio da parte del Server
    for entry in stub.GetAlladditionalServicesFlight(Managment_pb2.AdditionalServiceCostRequest(compagnia=compagnia)):
        #print(entry.prezzo)
        output.append(entry.prezzo)
    """
    output[0] = bagaglioSpeciale
    output[1] = bagaglioStivaMedio
    output[2] = bagaglioStivaGrande
    output[3] = assicurazioneBagagli
    output[4] = animaleDomestico
    output[5] = neonato
    """
    additionalServices = AdditionalServices(output[0], output[1], output[2], output[3], output[4], output[5])
    
    return additionalServices




def sendNewFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.AddFlight(Managment_pb2.NewFlight(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    #we need to return the boolean value
    return output.isOk




def sendNewPrice(flightId, newPrice):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyFlight(Managment_pb2.UpdatedFlight(flightId=flightId, newPrice=newPrice))
    #we need to return the boolean value
    return output.isOk    





def sendSeatsPrices(airline, price1, price2, price6, price16, price18):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifySeats(Managment_pb2.UpdatedSeats(airline=airline, price1=price1, price2=price2, price6=price6, price16=price16, price18=price18))
    #we need to return the boolean value
    return output.isOk 




def sendServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyServices(Managment_pb2.UpdatedServices(airline=airline, priceBM=priceBM, priceBG=priceBG, priceBS=priceBS, priceAD=priceAD, priceAB=priceAB, priceTN=priceTN))
    #we need to return the boolean value
    return output.isOk 
