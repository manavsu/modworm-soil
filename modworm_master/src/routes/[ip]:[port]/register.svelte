<script lang="ts">
    import "$lib/app.css";
    import { ModbusDataType } from "$lib/modbus_data_type";
    
    export let value:string;
    export let address:number;
    export let type: ModbusDataType;
</script>

<div class="relative text-xl text-right p-2 my-2 mx-1 w-24 h-fit bg-gray-800 rounded-tr-md rounded-bl-md">
    <div class="absolute -top-2 left-1 text-gray-400 text-xs">{address}</div>
    <div class="absolute -bottom-2 right-1 text-gray-400 text-xs">{type}</div>
    {value}
</div>