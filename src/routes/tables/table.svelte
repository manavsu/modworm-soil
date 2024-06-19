<script>
    import Title from "$lib/title.svelte";
    import { BASE_URL } from "$lib/env";
    import { fade } from 'svelte/transition';
    import { Network, Socket } from "$lib/network";
    import { onMount } from "svelte";
    import { Working, ConnectedSocket} from "$lib/store";
    async function ScanTable() {
        const response = await fetch(`${BASE_URL}/mmap/`);
        if (!response.ok) {
        return await response.json();
    }
</script>