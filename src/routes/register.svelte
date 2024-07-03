<script lang="ts">
    import "$lib/app.css";
    import { ModbusDataType } from "$lib/modbus_data_type";
    
    export let value:string;
    export let address:number;
    export let type: ModbusDataType;
</script>

<div class="relative text-l text-right p-2 my-2 mx-1 w-24 border rounded-xl">
    <div class="absolute -top-3 left-1 text-gray-400 text-s">{address}</div>
    <div class="absolute -bottom-2 right-1 text-gray-400 text-xs">{type}</div>
    {value}
</div>