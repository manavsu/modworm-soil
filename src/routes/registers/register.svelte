<script lang="ts">
    import "$lib/app.css";
    import { ModbusDataType } from "$lib/modbus_data_type";
    
    export let value:string;
    export let address:number;
    export let type: ModbusDataType;
</script>

<div class="flex flex-row text-l p-2 mx-2 w-36 border-2 border-gray-600 rounded-xl items-center">
    <div class="flex flex-col text-right min-w-10">
        <div class="text-xs">{address}</div>
        <div class="text-xs">{type}</div>
    </div>
    <div class="border border-gray-600 ml-2 mr-4 min-h-8"></div>
    <div class="min-w-14 text-center">{value}</div>
</div>
