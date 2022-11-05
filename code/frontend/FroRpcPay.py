import grpc

from proto import Payment_pb2
from proto import Payment_pb2_grpc



ADDR_PORT = 'payment:50055'



def sendPayment(username, card, postiSelezionati, dataPagamento, prezzoBase, prezzoSelezionePosti, prezzoServiziAggiuntivi, prezzoTotale, serviziSelezionati, email):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Payment_pb2_grpc.PayStub(channel)

    #get response from Payment service
    output = stub.AddPayment(Payment_pb2.NewPayment(username=username, idVolo=card.idVolo, selectedSeats=postiSelezionati, paymentDate=dataPagamento, basePrice=prezzoBase, seatsPrice=prezzoSelezionePosti, servicesPrice=prezzoServiziAggiuntivi, totalPrice=prezzoTotale, numStivaMedi=serviziSelezionati.bagaglioStivaMedio, numStivaGrandi=serviziSelezionati.bagaglioStivaGrande, numBagagliSpeciali=serviziSelezionati.bagaglioSpeciale, numAssicurazioni=serviziSelezionati.assicurazioneBagagli, numAnimali=serviziSelezionati.animaleDomestico, numNeonati=serviziSelezionati.neonato, email=email))
    #we need to return the boolean value
    return output.isOk   
