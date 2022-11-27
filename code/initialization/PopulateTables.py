import boto3
import time

from decimal import *

dynamodb = boto3.resource('dynamodb')

def initializeVolo():
    table = dynamodb.Table('Volo')

    #storing all the fligths
    table.put_item(
        Item = {
            'Id': '0000000000',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '09:12AM',
            'Orario arrivo': '10:05AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("78"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000001',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '01:33PM',
            'Orario arrivo': '02:26PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("82"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000002',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '12:47PM',
            'Orario arrivo': '01:40PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("74"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000003',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '07:25PM',
            'Orario arrivo': '08:18PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("69"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000004',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '02:02PM',
            'Orario arrivo': '02:55PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("81"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000005',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '04:30PM',
            'Orario arrivo': '05:23PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("77.5"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000006',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '06:59AM',
            'Orario arrivo': '07:52AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("88"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000007',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '11:17AM',
            'Orario arrivo': '12:10PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("61"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000008',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '05:42AM',
            'Orario arrivo': '08:00AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("118"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000009',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '01:11PM',
            'Orario arrivo': '03:29PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("143.5"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000a',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '08:35PM',
            'Orario arrivo': '10:53PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("127"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000b',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '10:21AM',
            'Orario arrivo': '12:39PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("156"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000c',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '05:13PM',
            'Orario arrivo': '07:31PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("150"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000d',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '06:40AM',
            'Orario arrivo': '08:58AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("122"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000e',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '12:19PM',
            'Orario arrivo': '02:37PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("135.2"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000f',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '09:03AM',
            'Orario arrivo': '11:21AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("171"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000g',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Heathrow (Londra)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '04:44PM',
            'Orario arrivo': '07:02PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("130"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000h',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '02:25AM',
            'Orario arrivo': '04:31AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("108"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000i',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '06:51AM',
            'Orario arrivo': '08:57AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("109"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000j',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '09:40PM',
            'Orario arrivo': '11:46PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("135"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000k',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '07:15AM',
            'Orario arrivo': '09:21AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("111.1"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000l',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '12:40PM',
            'Orario arrivo': '14:46PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("99.9"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000l',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '11:09AM',
            'Orario arrivo': '12:15PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("115"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000m',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '01:38PM',
            'Orario arrivo': '03:44PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("126"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000n',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '08:14AM',
            'Orario arrivo': '10:20AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("112"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000o',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Fiumicino (Roma)',
            'Orario partenza': '06:56PM',
            'Orario arrivo': '09:02PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("97"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000p',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '12:48PM',
            'Orario arrivo': '13:41PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("68"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000q',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '03:06AM',
            'Orario arrivo': '03:59AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("75"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000r',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '09:17AM',
            'Orario arrivo': '10:10AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("88"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000s',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '07:36AM',
            'Orario arrivo': '08:29AM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("81.6"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000t',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '08:55AM',
            'Orario arrivo': '09:48AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("81"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000u',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '02:20PM',
            'Orario arrivo': '03:13PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("77"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000v',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '12:00PM',
            'Orario arrivo': '12:53PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("72"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000w',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '01:24PM',
            'Orario arrivo': '02:17PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("91"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000x',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Charles De Gaulle (Parigi)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '06:32PM',
            'Orario arrivo': '07:25PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("80.3"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000y',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '04:09AM',
            'Orario arrivo': '06:27AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("160"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000000z',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '10:44AM',
            'Orario arrivo': '01:02PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("153"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000010',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '08:21AM',
            'Orario arrivo': '10:39AM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("135"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000011',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '03:19PM',
            'Orario arrivo': '05:37PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("146"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000012',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '12:38PM',
            'Orario arrivo': '02:56PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("171"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000013',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '07:01AM',
            'Orario arrivo': '09:19AM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("159.8"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000014',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '11:49AM',
            'Orario arrivo': '02:07PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("159"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000015',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '05:56AM',
            'Orario arrivo': '08:14AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("143"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000016',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Heathrow (Londra)',
            'Orario partenza': '05:22PM',
            'Orario arrivo': '07:40PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("169"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000017',
            'Data': '22-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '06:31AM',
            'Orario arrivo': '08:37AM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("123"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000018',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '04:47AM',
            'Orario arrivo': '06:53AM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("120"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '0000000019',
            'Data': '23-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '11:16AM',
            'Orario arrivo': '01:22PM',
            'Compagnia aerea': 'ITA',
            'Prezzo base': Decimal("134"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000001a',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '10:00AM',
            'Orario arrivo': '12:06PM',
            'Compagnia aerea': 'EasyJet',
            'Prezzo base': Decimal("147"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000001b',
            'Data': '24-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '04:12PM',
            'Orario arrivo': '06:18PM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("122"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000001c',
            'Data': '25-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '02:33AM',
            'Orario arrivo': '04:39AM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("105"),
            'Liberi': 156
        }
    )

    table.put_item(
        Item = {
            'Id': '000000001d',
            'Data': '26-12-2022',
            'Aeroporto partenza': 'Fiumicino (Roma)',
            'Aeroporto arrivo': 'Charles De Gaulle (Parigi)',
            'Orario partenza': '08:41AM',
            'Orario arrivo': '10:47AM',
            'Compagnia aerea': 'Ryanair',
            'Prezzo base': Decimal("104"),
            'Liberi': 156
        }
    )

def initializePostiOccupati():
    table = dynamodb.Table('PostiOccupati')

    #storing all the busy seats
    table.put_item(
        Item = {
            'IdVolo': '0000000000',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000001',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000002',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000003',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000004',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000005',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000006',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000007',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000008',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000009',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000a',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000b',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000c',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000d',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000e',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000f',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000g',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000h',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000i',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000j',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000k',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000l',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000m',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000n',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000o',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000p',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000q',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000r',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000s',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000t',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000u',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000v',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000w',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000x',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000y',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000000z',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000010',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000011',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000012',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000013',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000014',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000015',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000016',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000017',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000018',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '0000000019',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000001a',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000001b',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000001c',
        }
    )

    table.put_item(
        Item = {
            'IdVolo': '000000001d',
        }
    )

def initializePrezzoPosti():
    table = dynamodb.Table('PrezzoPosti')

    #storing all the prices
    table.put_item(
        Item = {
            'Compagnia': 'EasyJet',
            '1': Decimal("15"),
            '2-5': Decimal("13"),
            '6-15': Decimal("7"),
            '16-17': Decimal("15"),
            '18-26': Decimal("3")
        }
    )

    table.put_item(
        Item = {
            'Compagnia': 'ITA',
            '1': Decimal("15"),
            '2-5': Decimal("13"),
            '6-15': Decimal("7"),
            '16-17': Decimal("15"),
            '18-26': Decimal("3")
        }
    )

    table.put_item(
        Item = {
            'Compagnia': 'Ryanair',
            '1': Decimal("15"),
            '2-5': Decimal("13"),
            '6-15': Decimal("7"),
            '16-17': Decimal("15"),
            '18-26': Decimal("3")
        }
    )

def initializeServizi():
    table = dynamodb.Table('Servizi')

    #storing all the prices
    table.put_item(
        Item = {
            'Compagnia': 'EasyJet',
            'Bagaglio in stiva medio': Decimal("60"),
            'Bagaglio in stiva grande': Decimal("75"),
            'Bagaglio speciale': Decimal("50"),
            'Animale domestico': Decimal("50"),
            'Assicurazione bagagli': Decimal("10"),
            'Neonato': Decimal("75")
        }
    )

    table.put_item(
        Item = {
            'Compagnia': 'ITA',
            'Bagaglio in stiva medio': Decimal("60"),
            'Bagaglio in stiva grande': Decimal("75"),
            'Bagaglio speciale': Decimal("50"),
            'Animale domestico': Decimal("50"),
            'Assicurazione bagagli': Decimal("10"),
            'Neonato': Decimal("75")
        }
    )

    table.put_item(
        Item = {
            'Compagnia': 'Ryanair',
            'Bagaglio in stiva medio': Decimal("60"),
            'Bagaglio in stiva grande': Decimal("75"),
            'Bagaglio speciale': Decimal("50"),
            'Animale domestico': Decimal("50"),
            'Assicurazione bagagli': Decimal("10"),
            'Neonato': Decimal("75")
        }
    )

time.sleep(120)
initializeVolo()
initializePostiOccupati()
initializePrezzoPosti()
initializeServizi()
