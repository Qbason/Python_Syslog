import React from 'react'
import axios from 'axios';


export default function Main() {


    const ip_address = process.env.REACT_APP_IP_ADDRESS//"http://127.0.0.1:8000/"

    const [filters,setFilters] = React.useState(
        {
            "timefilter":"",
            "contentfilter":"",
            "typesfilter":""
        }
    )
    

    const [devices,setDevices] = React.useState(
        []
    )
    const [logs,setLogs] = React.useState(
        []
    )

    const [actualDeviceDate,setActualDeviceDate] = React.useState(
        {
            "deviceId":"",
            "date":""
        }
    )


    React.useEffect(()=>{

        const ip_address_device = ip_address+"api/device/"

        const getAllDevices = async ()=>{

            await axios.get(ip_address_device).then(
                res=>{
                    setDevices(
                        res.data
                    )
                }
            )
        }

        getAllDevices()

    },[])


    React.useEffect(()=>{

        if (devices.length>0){
                        
            setActualDeviceDate(
                (prev)=>{
                    console.log(
                        devices[0].id
                    )
                    return {
                        ...prev,
                        "deviceId":devices[0].id
                    }
                }
            )
        }

    },[devices])

    React.useEffect(()=>{

        const ip_address_log = ip_address+"api/log/"
        const getAllLogs = async ()=>{

            if (actualDeviceDate.deviceId!=="" && actualDeviceDate.date!==""){

                const url = new URL(ip_address_log)

                url.searchParams.set('search',actualDeviceDate.date)
                url.searchParams.set('device',actualDeviceDate.deviceId)

                axios.get(url).then(
                    res=>{
                        setLogs(
                            res.data
                        )
                    }
                )

            }



        }
        getAllLogs()


    },[actualDeviceDate])

    const options = devices.map(

        (element)=>{

            return <option key={element.id} value={element.id}>{element.ipaddress}</option>
        }

    )

    const trlogs = logs.filter(

        (element)=>{
            return (element.datetime.indexOf(filters.timefilter)!==-1)&&
            (element.content.indexOf(filters.contentfilter)!==-1)&&
            (element.types.indexOf(filters.typesfilter)!==-1)
        }

    ).map(

        (element)=>{
            return (
                <tr key={element.id}>
                    <td>{element.datetime}</td>
                    <td>{element.types}</td>
                    <td>{element.content}</td>
                </tr>
            )
        }

    )

    const changeValue = (e)=>{

        const {name,value} = e.target

        setActualDeviceDate(
            (prev)=>{
                return {
                    ...prev,
                    [name]:value
                }
            }
        )

    }

    const changeValueFilter = (e)=>{

        const {name,value} = e.target

        setFilters(
            (prev)=>{
                return {
                    ...prev,
                    [name]:value
                }
            }
        )


    }


  return (
    <main className='main'>
        

        <div className='form'>

            <div className='filters'>
                <div className="selector">
                    <select className="selector--select" name="deviceId" value={actualDeviceDate.deviceId} onChange={changeValue}>
                        {options}
                    </select>
                    <input className="selector--input" name="date" type="date" value={actualDeviceDate.date} onChange={changeValue} />
                </div>
                <div className="searcher">
                    <input className="searcher--input" onChange={changeValueFilter} name="timefilter" value={filters.timefilter} type="text" placeholder='Type time'/>
                    <input className="searcher--input" onChange={changeValueFilter} name="contentfilter" value={filters.contentfilter} type="text" placeholder='Type content'/>
                    <input className="searcher--input" onChange={changeValueFilter} name="typesfilter" value={filters.typesfilter} type="text" placeholder='Type type'/>

                </div>
            </div>
            <div className="content">
                <table className='table'>
                    <thead>
                        <tr>
                            <th>Date time</th>
                            <th>Types</th>
                            <th>Content</th>
                        </tr>
                    </thead>
                    <tbody>
                        {trlogs}
                    </tbody>

                </table>
            </div>
        </div>


    </main>
  )
}
